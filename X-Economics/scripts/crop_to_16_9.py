#!/usr/bin/env python3
import os
import glob
from PIL import Image

def crop_center_16_9(image_path, output_path=None):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} does not exist.")
        return False
        
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width == 1024 and height == 1024:
                # Target dimensions for 16:9 with width 1024
                target_width = 1024
                target_height = 576
                
                # Center crop coordinates
                left = 0
                top = (height - target_height) // 2  # (1024 - 576) // 2 = 224
                right = width
                bottom = top + target_height         # 224 + 576 = 800
                
                cropped_img = img.crop((left, top, right, bottom))
                
                if output_path is None:
                    output_path = image_path
                    
                # Save cropped image (overwrite or new path)
                cropped_img.save(output_path, "PNG")
                print(f"✅ Successfully cropped {os.path.basename(image_path)} to 16:9 ({target_width}x{target_height}) -> {output_path}")
                return True
            else:
                print(f"⚠️ Skip: {os.path.basename(image_path)} has dimensions {width}x{height} (not 1024x1024)")
                return False
    except Exception as e:
        print(f"❌ Error cropping {os.path.basename(image_path)}: {e}")
        return False

def main():
    target_dir = "/Users/pro16/Documents/VideoProject/X-Economics/episodes/showbiz_drugs_economics/images"
    
    # 6 core generated images to crop
    target_filenames = [
        "factory_vs_star.png",
        "stock_chart_comparison.png",
        "propofol_scale_comparison.png",
        "storefront_billboard.png",
        "virtual_influencer_studio.png",
        "closing_shot.png"
    ]
    
    print("=" * 60)
    print("🎬 CROPPING IMAGES TO 16:9 (1024x576) FOR VIDEO PRODUCTION")
    print("=" * 60)
    
    for filename in target_filenames:
        path = os.path.join(target_dir, filename)
        # Create a backup of the original square image
        backup_path = os.path.join(target_dir, f"original_{filename}")
        if os.path.exists(path) and not os.path.exists(backup_path):
            try:
                # Copy original to backup
                with open(path, "rb") as src, open(backup_path, "wb") as dst:
                    dst.write(src.read())
                print(f"💾 Created backup: original_{filename}")
            except Exception as e:
                print(f"Failed to create backup: {e}")
                
        # Perform crop (modifies the target file in-place)
        crop_center_16_9(path)
        
    print("=" * 60)
    print("Done!")

if __name__ == "__main__":
    main()
