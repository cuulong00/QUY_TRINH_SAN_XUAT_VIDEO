Build a custom web application called "Google Flow Advanced Storyboard Director" to manage and execute multi-track creative generation campaigns. The application should have a high-end dark mode glassmorphic UI, an asynchronous queue controller, and support modern browser APIs for local file management.

### 1. User Interface & Layout (Glassmorphism Theme)
- Theme: Dark anthracite background (#0b0c10) with soft violet (#8b5cf6) and cyan (#06b6d4) neon gradient orbs in the background.
- Panels: Semi-transparent glassmorphic panels with rounded corners (16px) and thin borders (rgba(255,255,255,0.08)).
- Left Panel (Control & Pipeline Setup):
  - A file picker to upload a pipeline prompt list (.txt or .json).
  - A directory picker button labeled "Set Project Destination Folder" (using the File System Access API) to select a local directory on the user's computer.
  - Dropdown "Select Video Model" (options: Veo 3.1, Veo 3.0, Veo Beta).
  - Dropdown "Select Image Model" (options: Imagen 4, Imagen 3, Nano Banana Pro).
  - Slider for "Max Concurrent Active Tracks" (range 1 to 6, default 4).
  - Slider for "Delay between Triggers" (range 2s to 15s, default 6s).
  - Stats block showing: Total Scenes, Completed, and Pending counts.
  - Controls: "Start Pipeline", "Pause Pipeline", "Reset".
- Right Panel (Active Tracks Monitor):
  - Responsive grid layout displaying cards for active tracks up to the slider limit. Empty slots show "Idle". 
  - Active slot cards show slot number, scene ID, asset type (Image/Video), prompt preview, a running countdown, and a smooth linear progress bar.
  - Each active track card displays a thumbnail preview of the mapped "Reference Image (Ingredient)" if configured, and a prominent "Copy Prompt" button.
- Bottom Panel (Full Storyboard Table):
  - Scrollable list of parsed scenes (columns: STT, Scene ID, Type [Image/Video], Mapped Reference, Prompt text, Status [Pending, Waiting, Active, Completed]). Includes a search bar to filter entries.

### 2. Script & Pipeline Parsing Logic
- Support loading text files (.txt) or configuration JSON files (.json).
- Automatically parse lines to extract Scene ID, Target Type (Image or Video), Mapped Reference Image, and the Prompt text.
  * Example Text Line (Video): "c1-1 (V) [ref: car_blue.png]: A steady cinematic shot of a blue car..."
  * Example Text Line (Image): "c1-2 (I) [ref: avatar_face.png]: A high-resolution headshot of..."
- Maintain a structured array of scene objects: { index, id, type ('image'|'video'), referenceImage, promptText, status ('pending') }.

### 3. File System Access API & Auto-Save
- Implement a click handler for "Set Project Destination Folder" that calls `window.showDirectoryPicker()` to request write access to a local directory.
- When an asset generation completes:
  1. Programmatically capture the generated asset (blob).
  2. Auto-save the file directly to the authorized local directory using `FileSystemDirectoryHandle.getFileHandle()`.
  3. Automatically name the file based on the Scene ID and format (e.g., "c1-1.mp4" for videos, "c1-2.png" for images), bypass the default downloads folder, and save it in the background.

### 4. Reference Image Mapping & Queue Logic
- Allow users to drag and drop multiple reference images into a sidebar bin.
- Match uploaded image filenames to the "Mapped Reference Image" property in the parsed pipeline configuration.
- Queue Controller Flow:
  * When "Start Pipeline" is clicked, run the dispatch loop.
  * Pull the next pending scene. Set status to "Waiting" and run the countdown timer.
  * When the countdown ends:
    1. Update state to "Active" and trigger generation based on the scene "Type" (Image or Video) using the configured Model (e.g., Veo 3.1 for video, Imagen 4 for image).
    2. Attach the mapped local reference image as an "Ingredient" to the generation payload.
    3. Copy the promptText to the OS clipboard, play a gentle notification sound, and show a toast alert: "Prompt copied & reference image mapped!".
    4. Simulates a rendering countdown (8s for video, 3s for image).
  * On completion, auto-save the generated file, set status to 'completed', and free the slot to process the next queue item.
