%global forgeurl https://github.com/ghostty-org/ghostty/
%global tag v1.0.0
%global ghosttybuild /tmp/ghostty
%forgemeta

Name: ghostty
Version: 1.0.0
Release: 1%{?dist}
Summary: Fast, native, feature-rich terminal emulator pushing modern features.

License: MIT
URL: https://ghostty.org
Source: %{forgesource}

BuildRequires: zig
BuildRequires: glib2-devel
BuildRequires: pandoc
BuildRequires: freetype-devel
BuildRequires: harfbuzz-devel
BuildRequires: fontconfig-devel
BuildRequires: libpng-devel
BuildRequires: oniguruma-devel
BuildRequires: libadwaita-devel

%description
Ghostty is a terminal emulator that differentiates itself by being fast, feature-rich, and native. While there are many excellent terminal emulators available, they all force you to choose between speed, features, or native UIs. Ghostty provides all three.

In all categories, I am not trying to claim that Ghostty is the best (i.e. the fastest, most feature-rich, or most native). But Ghostty is competitive in all three categories and Ghostty doesn't make you choose between them.

Ghostty also intends to push the boundaries of what is possible with a terminal emulator by exposing modern, opt-in features that enable CLI tool developers to build more feature rich, interactive applications.

While aiming for this ambitious goal, our first step is to make Ghostty one of the best fully standards compliant terminal emulator, remaining compatible with all existing shells and software while supporting all of the latest terminal innovations in the ecosystem. You can use Ghostty as a drop-in replacement for your existing terminal emulator.

%prep
%forgesetup

%build
mkdir -p %{ghosttybuild}%{_prefix}

ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache ./nix/build-support/fetch-zig-cache.sh

zig build \
  --prefix %{ghosttybuild}%{_prefix} \
  --system /tmp/offline-cache/p \
  -Doptimize=ReleaseFast \
  -Dcpu=baseline

%install

install -Dpm 0755 %{ghosttybuild}%{_bindir}/ghostty %{buildroot}%{_bindir}/ghostty
install -Dpm 0644 %{ghosttybuild}%{_datadir}/applications/com.mitchellh.ghostty.desktop %{buildroot}%{_datadir}/applications/com.mitchellh.ghostty.desktop
install -Dpm 0644 %{ghosttybuild}%{bash_completions_dir}/ghostty.bash %{buildroot}%{bash_completions_dir}/ghostty.bash
install -Dpm 0644 %{ghosttybuild}%{_datadir}/bat/syntaxes/ghostty.sublime-syntax %{buildroot}%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
install -Dpm 0644 %{ghosttybuild}%{fish_completions_dir}/ghostty.fish %{buildroot}%{fish_completions_dir}/ghostty.fish
for docfile in $(find %{ghosttybuild}%{_datadir}/ghostty/doc -type f); do
  install -Dpm 0644 "$docfile" %{buildroot}%{_datadir}/ghostty/doc/$(basename "$docfile")
done
install -Dpm 0644 %{ghosttybuild}%{_datadir}/ghostty/shell-integration/bash/bash-preexec.sh %{buildroot}%{_datadir}/ghostty/shell-integration/bash/bash-preexec.sh
install -Dpm 0644 %{ghosttybuild}%{_datadir}/ghostty/shell-integration/bash/ghostty.bash %{buildroot}%{_datadir}/ghostty/shell-integration/bash/ghostty.bash
install -Dpm 0644 %{ghosttybuild}%{_datadir}/ghostty/shell-integration/elvish/lib/ghostty-integration.elv %{buildroot}%{_datadir}/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
install -Dpm 0644 %{ghosttybuild}%{_datadir}/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish %{buildroot}%{_datadir}/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
install -Dpm 0644 %{ghosttybuild}%{_datadir}/ghostty/shell-integration/zsh/ghostty-integration %{buildroot}%{_datadir}/ghostty/shell-integration/zsh/ghostty-integration
for themefile in $(find %{ghosttybuild}%{_datadir}/ghostty/themes -type f); do
  [ -f "$themefile" ] && install -Dpm 0644 "$themefile" %{buildroot}%{_datadir}/ghostty/themes/$(basename "$themefile")
done
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
install -Dpm 0644 %{ghosttybuild}%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop %{buildroot}%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop
install -Dpm 0644 %{ghosttybuild}%{_mandir}/man1/ghostty.1 %{buildroot}%{_mandir}/man1/ghostty.1
install -Dpm 0644 %{ghosttybuild}%{_mandir}/man5/ghostty.5 %{buildroot}%{_mandir}/man5/ghostty.5
install -Dpm 0644 %{ghosttybuild}%{_datadir}/nvim/site/ftdetect/ghostty.vim %{buildroot}%{_datadir}/nvim/site/ftdetect/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/nvim/site/ftplugin/ghostty.vim %{buildroot}%{_datadir}/nvim/site/ftplugin/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/nvim/site/syntax/ghostty.vim %{buildroot}%{_datadir}/nvim/site/syntax/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/terminfo/ghostty.termcap %{buildroot}%{_datadir}/terminfo/ghostty.termcap
install -Dpm 0644 %{ghosttybuild}%{_datadir}/terminfo/ghostty.terminfo %{buildroot}%{_datadir}/terminfo/ghostty.terminfo
install -Dpm 0644 %{ghosttybuild}%{_datadir}/terminfo/g/ghostty %{buildroot}%{_datadir}/terminfo/g/ghostty
install -Dpm 0644 %{ghosttybuild}%{_datadir}/terminfo/x/xterm-ghostty %{buildroot}%{_datadir}/terminfo/x/xterm-ghostty
install -Dpm 0644 %{ghosttybuild}%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim %{buildroot}%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/vim/vimfiles/syntax/ghostty.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/ghostty.vim
install -Dpm 0644 %{ghosttybuild}%{_datadir}/zsh/site-functions/_ghostty %{buildroot}%{_datadir}/zsh/site-functions/_ghostty

%files

%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{bash_completions_dir}/ghostty.bash
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{fish_completions_dir}/ghostty.fish
%{_datadir}/ghostty/doc/*
%{_datadir}/ghostty/shell-integration/bash/bash-preexec.sh
%{_datadir}/ghostty/shell-integration/bash/ghostty.bash
%{_datadir}/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
%{_datadir}/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
%{_datadir}/ghostty/shell-integration/zsh/ghostty-integration
%{_datadir}/ghostty/themes/*
%{_datadir}/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/nvim/site/ftdetect/ghostty.vim
%{_datadir}/nvim/site/ftplugin/ghostty.vim
%{_datadir}/nvim/site/syntax/ghostty.vim
%{_datadir}/terminfo/ghostty.termcap
%{_datadir}/terminfo/ghostty.terminfo
%{_datadir}/terminfo/g/ghostty
%{_datadir}/terminfo/x/xterm-ghostty
%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
%{_datadir}/vim/vimfiles/syntax/ghostty.vim
%{_datadir}/zsh/site-functions/_ghostty

%define debug_package %{nil}

%changelog
%autochangelog
