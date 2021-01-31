# PlandoRandomSettings

This program is a custom version of the [*Ocarina of Time* randomzier](https://ootrandomizer.com/) that can apply random values to each of the randomizer settings.
This program allows us to blindly randomize anything and (nearly) everything in the randomizer, rather than just the natively supported random settings.

## Download

* [Windows (64-bit)](https://github.com/matthewkirby/plando-random-settings/releases/latest/download/rsl-win64.exe)
* [macOS (Intel)](https://github.com/matthewkirby/plando-random-settings/releases/latest/download/rsl-mac-intel.dmg)
* For other platforms, [request support](https://github.com/matthewkirby/plando-random-settings/issues/new) or [build from source](#building-from-source).

## Usage

When opening the app, you will see the following from top to bottom:

1. The app checks for self-updates when opened. It is recommended that you always update to the latest available version, since older versions may break with newer versions of the randomizer.
2. For the Base ROM, select your copy of *Ocarina of Time*. Please see [the randomizer's readme](https://github.com/TestRunnerSRL/OoT-Randomizer#installation) for details.
3. For the Output Directory, select a folder where the files generated by the randomizer should be saved.
4. Next, select your preferred weights (i.e. how likely each value of each setting will be). The options are:
    * **League:** The Random Settings League's season 2 tournament weights. Uses [version 5.2.117 R-1](https://github.com/Roman971/OoT-Randomizer/tree/b670183e9aff520c20ac2ee65aa55e3740c5f4b4) of the randomizer. See [this file](https://github.com/matthewkirby/plando-random-settings/blob/master/assets/weights/rsl.json) for the full list.
    * **Solo:** Like League weights but uses the latest version of the randomizer.
    * **Co-op:** Limits the maximum number of required skull tokens to 50, disables Master Quest, and fixes the damage multiplier to normal.
    * **Multiworld:** This disables settings that can cause seeds to take a long time, such as closed Door of Time, Overworld entrance randomizer, or useless hints. It also disables Skip Child Zelda to avoid [this bug](https://github.com/TestRunnerSRL/OoT-Randomizer/issues/1210).
    * **Custom:** Allows you to fully customize the weights.
5. For League weights, there are no further options, to avoid accidental misconfigurations. For other presets, you can now optionally remove tricks from logic and/or turn off the possibility of starting with random items. For custom weights, configure them to your liking. You can also export them to a file, or import weights from a file.
6. For Multiworld weights, select the number of players (also called the world count) using the slider or text box.
7. Click “Generate Seed”. This can occasionally take a while, since it makes 60 attempts at generating a seed (20 distributions, each tried 3 times). Once done, the output directory will contain the patch file that you can send to the players (or apply the patch for yourself with [the randomizer](https://ootrandomizer.com/generator) by selecting “Generate From Patch File”), as well as the spoiler log and a copy of the settings distributions (which is also considered a spoiler in the Random Settings League).

## Building from source

1. Install Rust:
    * On Windows, download and run [rustup-init.exe](https://win.rustup.rs/) and follow its instructions.
    * On other platforms, please see [the Rust website](https://www.rust-lang.org/learn/get-started) for instructions.
2. (Skip this step if you're not on Windows.) If you're on Windows, you'll also need to download and install [Visual Studio](https://visualstudio.microsoft.com/vs/) (the Community edition should work). On the “Workloads” screen of the installer, make sure “Desktop development with C++” is selected. (Note that [Visual Studio Code](https://code.visualstudio.com/) is not the same thing as Visual Studio. You need VS, not VS Code.)
3. Install [Python](https://python.org/) version 3.6 or higher.
4. Open a command line:
    * On Windows, right-click the start button, then click “Windows PowerShell” or “Command Prompt”.
    * On other platforms, look for an app named “Terminal” or similar.
5. In the command line, run the following command. Depending on your computer, this may take a while.

    ```
    cargo install --git=https://github.com/fenhl/plando-random-settings --branch=riir
    ```
6. You can now launch the app by running the command `rsl-gui`, or use the command-line version `rsl` (see `rsl --help` for details).

## Releasing a new version

You will need a 64-bit Windows PC and an Intel Mac.

1. On macOS:
    1. Install [Rust](https://rust-lang.org/) and [Python](https://python.org/).
    2. Clone this repo.
    3. In System Preferences → Sharing, make sure Remote Login is enabled and you have access.
2. On Windows:
    1. [Create a GitHub personal access token](https://github.com/settings/tokens/new) with the public_repo scope.
    1. Install [Rust](https://rust-lang.org/) and [Python](https://python.org/).
    2. Clone this repo.
    3. In the repo clone, create a [JSON](https://json.org/) file at `assets/release-config.json` with the following entries:
        * `"githubToken"`: The personal access token from step 1
        * `"macHostname"`: A hostname or IP address at which your Mac is reachable via SSH (and if necessary the username, in `"username@hostname"` form)
        * `"macRepoPath"`: The path to the clone of this repo on your Mac
        * `"releaseNotesEditor"`: A command that will be called with `--wait` and the path to an empty file for writing the release notes (optional, defaults to `"C:\\Program Files\\Microsoft VS Code\\bin\\code.cmd"`)
        * `"repoOwner"`: The GitHub user or org where the release should be published (optional, defaults to `"matthewkirby"`)
        * `"repoName"`: The name of the repository where the release should be published (optional, defaults to `"plando-random-settings"`)
    4. In the repo, run `cargo run --release --package=rsl-utils --bin=rsl-release`. You can add the following command-line options, but must separate them with a `--` (so they're interpreted as `rsl-release` options, not `cargo` options):
        * To see output of build commands as they are happening, use `--verbose`. Note that this may considerably slow down the release script since it won't run multiple build commands in parallel.
        * To create the GitHub release as a draft but not publish it, use `--no-publish`.
