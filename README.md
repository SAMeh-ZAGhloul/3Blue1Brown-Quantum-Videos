
This project contains the code used to generate the explanatory math videos found on [3Blue1Brown](https://www.3blue1brown.com/).

This almost entirely consists of scenes generated using the library [Manim](https://github.com/3b1b/manim).  See also the community maintained version at [ManimCommunity](https://github.com/ManimCommunity/manim/).

Older projects may have code dependent on older versions of manim, and so may not run out of the box here.

## Recent Fixes and Updates

### 1. Path Configuration Fix

Fixed the path configuration in `custom_config.yml` to match the current directory structure:
- Changed `removed_mirror_prefix` from `/Users/grant/cs/videos/` to `/Users/user/Downloads/3Blue1Brown_videos/`
- Changed `base` to match the current directory

### 2. ThreeDAxes Patch

Created a patch for the `ThreeDAxes` class to add the missing `get_x_unit_size` method that's required by the `VectorField` class:

```python
class PatchedThreeDAxes(ThreeDAxes):
    """
    Extended version of ThreeDAxes that adds the get_x_unit_size method
    required by VectorField.
    """

    def get_x_unit_size(self):
        """
        Returns the unit size of the x-axis.
        This method is required by VectorField.
        """
        return self.x_axis.get_unit_size()

    def get_y_unit_size(self):
        """
        Returns the unit size of the y-axis.
        """
        return self.y_axis.get_unit_size()

    def get_z_unit_size(self):
        """
        Returns the unit size of the z-axis.
        """
        return self.z_axis.get_unit_size()
```

### 3. TimeVaryingVectorField Parameter Fixes

Fixed parameter issues in the `polarization.py` file:
- Changed `x_density` to `density`
- Changed `color` to `stroke_color`
- Properly configured the axes to have the correct range and density

### 4. Missing Module Creation

Created the missing modules:
- `_2025/blocks_and_grover/qc_supplements.py` - Contains utility functions for quantum computing visualizations
- `_2025/blocks_and_grover/state_vectors.py` - Contains classes for visualizing quantum state vectors

## Troubleshooting

### Common Issues

1. **Path Configuration Issues**: If you encounter path-related errors like:
   ```
   ValueError: '/path/to/file.py' is not in the subpath of '/different/path' OR one path is relative and the other is absolute.
   ```
   Check the `custom_config.yml` file and ensure the paths match your local environment.

2. **Missing Modules**: If you get "ModuleNotFoundError", make sure all required modules are in the correct directories.

3. **ThreeDAxes Issues**: If you encounter errors related to `ThreeDAxes` not having a `get_x_unit_size` method, make sure you're using the patched version from `axes_patch.py`.

4. **SVG Loading Errors**: If SVG files fail to load, the code includes fallback options that will use simple shapes instead.

### Running the Animations

To run a specific scene from one of the files, use the following command:

```bash
python3 -m manimlib _2025/grover/file_name.py
```

This will display a list of available scenes in the file. You can then select which scene to render by entering its number or name.

Note, while the library Manim itself is [open source](https://opensource.org/osd) software and under the [MIT license](https://github.com/3b1b/manim/blob/master/LICENSE.md), the contents of this repository are available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

## Workflow

I made [this video](https://youtu.be/rbu7Zu5X1zI) to show more of how I use manim. Note that I'm using 3b1b/manim, not the community edition, some functionality may differ between the two. Aside from [installing manim itself](https://github.com/3b1b/manim?tab=readme-ov-file#installation), replicating the workflow involves some custom plugins with Sublime, the text editor I use.

If you use another text editor, the same functionality can be mimicked. The key is to make use of two facts.

- Running `manimgl (file name) (scene name) -se (line_number)` will drop you into an interactive mode at that line of the file, like a debugger, with an iPython terminal that can be used to interact with the scene.

- Within that interactive mode, if you enter "checkpoint_paste()" to the terminal, it will run whatever bit of code is copied to the clipboard. Moreover, if that copied code begins with a comment, the first time it sees that comment it will save the state of the scene at that point, and for all future calls on code beginning with the same comment, it will first revert to that state of the scene before running the code.
    - The argument "skip" of checkpoint_paste will mean it runs the code without animating, as if all run times set to 0.
    - The argument "record" of checkpoint_paste will cause whatever animations are run with that copied code to be rendered to file.

For my own workflow, I set up some keyboard shortcuts to kick off each of these commands. For those who want to try it out themselves, here's what's involved.

### Sublime-specific instructions

Install [Terminus](https://packagecontrol.io/packages/Terminus) (via package control). This is a terminal run within sublime, and it lets us write some plugins that take the state in sublime, like where your cursor is, what's highlighted, etc., and use that to run a desired command line instruction.

Take the files in the "sublime_custom_commands" sub-directory of this repo, and copy them into the Packages/User/ directory of your Sublime Application. This should be a directory with a path that looks something like /wherever/your/sublime/lives/Packages/User/

Add some keybindings to reference these commands. Here's what I have inside my key_bindings file, you can find your own under the menu Sublime Text -> Settings -> Keybindings

```
    { "keys": ["shift+super+r"], "command": "manim_run_scene" },
    { "keys": ["super+r"], "command": "manim_checkpoint_paste" },
    { "keys": ["super+alt+r"], "command": "manim_recorded_checkpoint_paste" },
    { "keys": ["super+ctrl+r"], "command": "manim_skipped_checkpoint_paste" },
    { "keys": ["super+e"], "command": "manim_exit" },
    { "keys": ["super+option+/"], "command": "comment_fold"},
```

For example, I bind the "command + shift + R" to a custom "manim_run_scene" command. If the cursor is inside a line of a scene, this will drop you into the interactive mode at that point of the scene. If the cursor is on the line defining the scene, it will copy to the clipboard the command needed to render that full scene to file.

I bind "command + R" to a "manim_checkpoint_paste" command, which will copy whatever bit of code is highlighted, and run "checkpoint_paste()" in the interactive terminal.

Of course, you could set these to whatever keyboard shortcuts you prefer.

Copyright © 2024 3Blue1Brown
