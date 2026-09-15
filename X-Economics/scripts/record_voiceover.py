#!/usr/bin/env python3
"""
Bridge Caller for Production Voiceover (TTS) in X-Economics.
Calls the centralized engine at /Users/pro16/Documents/Code/TTS/run_production.py
without duplicating TTS dependencies or phonetic libraries in X-Economics.
"""

import os
import sys
import subprocess
import argparse

# Path to centralized TTS project
TTS_ENGINE_PATH = "/Users/pro16/Documents/Code/TTS/run_production.py"
XECONOMICS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def resolve_episode_dir(episode_arg):
    """Resolve episode input to absolute path within X-Economics."""
    if os.path.isabs(episode_arg) and os.path.isdir(episode_arg):
        return episode_arg
    
    # Check if relative to cwd
    if os.path.isdir(episode_arg):
        return os.path.abspath(episode_arg)
        
    # Check episodes/<slug>
    ep_path = os.path.join(XECONOMICS_ROOT, "episodes", episode_arg)
    if os.path.isdir(ep_path):
        return ep_path
        
    # Check if slug given as 'episodes/slug'
    ep_path2 = os.path.join(XECONOMICS_ROOT, episode_arg)
    if os.path.isdir(ep_path2):
        return ep_path2
        
    return None

def main():
    if not os.path.exists(TTS_ENGINE_PATH):
        print(f"❌ Cannot locate centralized TTS engine at: {TTS_ENGINE_PATH}")
        print("Please verify /Users/pro16/Documents/Code/TTS exists.")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="X-Economics Production TTS Caller (delegates to Code/TTS)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("episode", type=str,
                        help="Episode slug or directory (e.g. 'byd-vs-toyota-no-america-strategy' or 'episodes/byd-vs-toyota-no-america-strategy')")
    parser.add_argument("--voice", type=str, default="mc_nam_refined_short",
                        help="Voice preset ID (default: mc_nam_refined_short)")
    parser.add_argument("--speed", type=float, default=0.9,
                        help="Speaking speed tempo (default: 0.9)")
    parser.add_argument("--temperature", type=float, default=0.5,
                        help="Sampling temperature (default: 0.5)")
    parser.add_argument("--num-step", type=int, default=64,
                        help="Diffusion inference steps (default: 64)")
    parser.add_argument("--chapters", type=str, default=None,
                        help="Comma-separated chapter numbers (e.g., 1,3 or 1-5)")
    parser.add_argument("--normalize-only", action="store_true", default=False,
                        help="Only clean headers and apply phonetic rules directly to chapter files without TTS")
    parser.add_argument("--audit-only", action="store_true", default=False,
                        help="Audit chapter scripts for formatting, metric units, and sentence length")
    parser.add_argument("--local", action="store_true", default=False,
                        help="Run locally on Mac GPU (MPS) instead of RunPod GPU")
    parser.add_argument("--suffix", type=str, default=None,
                        help="Audio folder suffix (e.g., 'v2' creates audio_v2/)")

    # Capture known and unknown args to forward to engine
    args, unknown_args = parser.parse_known_args()

    episode_dir = resolve_episode_dir(args.episode)
    if not episode_dir:
        print(f"❌ Episode directory not found: '{args.episode}'")
        print(f"Searched under: {os.path.join(XECONOMICS_ROOT, 'episodes')}")
        sys.exit(1)

    # Build command to delegate to Code/TTS/run_production.py
    cmd = [
        "python3", TTS_ENGINE_PATH,
        episode_dir,
        "--voice", args.voice,
        "--speed", str(args.speed),
        "--temperature", str(args.temperature),
        "--num-step", str(args.num_step),
        "--no-cache"
    ]

    if args.chapters:
        cmd.extend(["--chapters", args.chapters])
    if args.normalize_only:
        cmd.append("--normalize-only")
    if args.audit_only:
        cmd.append("--audit-only")
    if args.local:
        cmd.append("--local")
    if args.suffix:
        cmd.extend(["--suffix", args.suffix])

    # Forward any other extra flags
    if unknown_args:
        cmd.extend(unknown_args)

    print(f"🎙️ [X-Economics Bridge] Calling Code/TTS Engine...")
    print(f"📂 Target Episode: {episode_dir}")
    print(f"🚀 Command: {' '.join(cmd)}\n")

    res = subprocess.run(cmd)
    sys.exit(res.returncode)

if __name__ == "__main__":
    main()
