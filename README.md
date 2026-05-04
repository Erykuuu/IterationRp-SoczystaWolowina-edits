# IterationRP Edit - V1.03 Patch

This repository provides a comprehensive patch for the **IterationRP Alpha 0.8.18** shader pack. This is a "whole edit" that overhaul many aspects of the shader, from cloud logic to post-processing and performance tuning.

Due to licensing, the original shader code cannot be distributed directly. Users must own the original shader zip to apply this edit.

## Key Changes and Improvements

### 🌤️ Atmosphere & Clouds
- **New Weather Engine**: Fully custom logic for transition and weather variety.
- **Advanced Cloud Mood System**: Optimized for manual control with refined mood influence.
- **Planar & Volumetric Cloud Overhaul**: Significant rewrites to `NUBIS.glsl` and `PlanarClouds.glsl` for better visuals and performance.
- **Improved Cloud Shadows**: Fixed Slant and range logic in `CloudShadow.glsl`.
- **New Rainbow System**: Added a high-quality atmospheric rainbow implementation.

### 🎨 Visuals & Post-Processing
- **Massive Final Pass Edit**: Large-scale optimizations and visual tweaks in `Final_FS.glsl`.
- **Custom LUT Support**: Added 4 distinct LUT slots for color grading with identity textures included.
- **Improved Temporal Dithering**: Refined noise handling for smoother visuals.
- **Volumetric Fog Tweaks**: Better height and density falloff transitions.

### ⚙️ Optimization & Defaults
- **PT IRC Optimized**: Sample per frame (SPP) set to 1 for better performance.
- **Cloud Quality Tuning**: Standardized to 2.0 for the best balance of speed and clarity.
- **Base Noise Scaling**: Adjusted to 0.001 for finer cloud details.
- **Disabled Grain/Noise**: Removed Film Grain and predictive weather networking by default for a cleaner look.

### 🖥️ User Interface
- **Expanded Menu**: 100+ lines of changes to `shaders.properties` to expose new controls.
- **Localized Labels**: Fully updated `en_us.lang` with descriptive labels for new features.

---

## How to Apply the Patch

### Requirements
- Python 3.x installed.
- Git installed (for `git apply` functionality).
- The original `iterationRP Alpha 0.8.18.zip` file.

### Instructions
1. Download `shader-patch.py` and `ITRPeditV1.03.diff` from this repository.
2. Place the original `iterationRP Alpha 0.8.18.zip` in the same folder.
3. Open a terminal/command prompt in that folder.
4. Run the following command:

```bash
python shader-patch.py "iterationRP Alpha 0.8.18.zip" "ITRPeditV1.03.diff" "ITRPedit_V1.03.zip"
```

5. The patched shader pack will be generated as `ITRPedit_V1.03.zip`. Move it to your Minecraft `shaderpacks` folder.

## Credits
- Original Shader: [IterationRP](https://github.com/Tahnass/IterationRP) by Tahnass.
- Patching Script based on: [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)
