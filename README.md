# sublime-gettext

[Sublime Text][st] support
for [`gettext`][gt] [Portable Object][po] (`.po`) files.


## Installation

### Package Control

1. Make sure you already have [Package Control][pc] installed.
2. Choose **Install Package** from the Command Palette
    (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>).
3. Type **Gettext** and press <kbd>Enter</kbd>.

With [auto_upgrade][] enabled,
Package Control will keep all installed packages up-to-date!

### Using Git

1. Change to your Sublime Text `Packages` directory.
2. Clone this repository.

### Manual installation

1. Download the latest ZIP file (*./archive/master.zip*).
2. Unzip the archive to your Sublime Text `Packages` directory.


## Usage

### Snippets

- `ctx` => Plural message in a context
- `hdr` => Header
- `id` => Message ID
- `idp` => Message ID plural
- `msg` => Simple Message
- `msgc` => Simple message in a context
- `msgcp` => Plural message in a context
- `msgp` => Plural message
- `str` => Message string
- `strp` => Message string plural


## Todo

- ~~Syntax regression tests~~
- ~~Investigate "range" flags~~
- Custom fold markers
- `printf` and other string formatting placeholders
- ~~Plurals mini-language in header~~
- Navigation by `fuzzy` or unfinished translations
- Toggle `fuzzy` flag


## Credits

- Snippets: [language-gettext](https://github.com/ArnaudRinquin/atom-language-gettext)

[st]: https://www.sublimetext.com
[gt]: https://www.gnu.org/software/gettext/
[po]: https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html
[pc]: https://packagecontrol.io
[auto_upgrade]: http://wbond.net/sublime_packages/package_control/settings/
