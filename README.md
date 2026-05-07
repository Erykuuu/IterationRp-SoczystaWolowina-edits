# IterationRP Edit - V1.10 Patch

This repository provides a patch for the **IterationRP Alpha 0.8.18** shader pack. Due to licensing, the original shader code cannot be distributed directly. Users must own the original shader zip to apply this edit.

## New in V1.10
- **Aurora Borealis System**: High-fidelity, performance-optimized dynamic aurora with organic movement.
- **Aurora Settings**: Dedicated AURORA tab in the menu with controls for master toggle, probability (frequency), and biome restriction (Snowy/Desert).
- **Atmospheric Storm Darkening**: Re-tuned cloud density and light absorption to provide a cinematic "blackout" effect during thunderstorms.
- **Cloud Animation Toggle**: New setting in the Volumetric Clouds menu to switch between **Frame Time** (continuous movement) and **World Time** (movement tied to in-game ticks).
- **Time Source Stability**: Fixed flickering and precision artifacts when using world-time synchronized clouds.

## Previous Changes (V1.04)
Dynamic Cloud System with different weathers
Reworked Godrays and Cloud Shadows
Cloud Godrays (similar to fog godrays but implemented into clouds for beautiful highlights)
Tweaked Cloud Visuals (Better scattered/planar clouds, more variations and randomness)
Flares (Both Anamorphic and Entopic)
Rainbows
Time Grade
Custom LUTs
Film Grain based on RGB noise
SSS Edits
Dynamic Biome color grading
Bokeh styles for Depth of field

## How to Apply the Patch

### Requirements
- Python 3.x installed.
- Git installed (for `git apply` functionality).
- The original `iterationRP Alpha 0.8.18.zip` file.

### Instructions
1. Download `shader-patch.py` and `ITRPeditV1.10.diff` from this repository.
2. Place the original `iterationRP Alpha 0.8.18.zip` in the same folder.
3. Open a terminal/command prompt in that folder.
4. Run the following command:

```bash
python shader-patch.py "iterationRP Alpha 0.8.18.zip" "ITRPeditV1.10.diff" "ITRPedit_V1.10.zip"
```

5. The patched shader pack will be generated as `ITRPedit_V1.10.zip`. You can now move this into your Minecraft `shaderpacks` folder.

## Credits
- Original Shader: [IterationRP](https://github.com/Tahnass/IterationRP)
- Patching Script based on: [huj31415/iterationrp-patches](https://github.com/huj31415/iterationrp-patches)
