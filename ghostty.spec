%global forgeurl https://github.com/ghostty-org/ghostty/
%global tag v1.0.0
%define debug_package %{nil}

%forgemeta

Name: ghostty
Version: 1.0.0
Release: 1%{?dist}
Summary: Fast, native, feature-rich terminal emulator pushing modern features.

License: MIT
URL: https://ghostty.org
Source: %{forgesource}

BuildRequires: zig
BuildRequires: gtk4-devel
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
ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache ./nix/build-support/fetch-zig-cache.sh

zig build \
  --system /tmp/offline-cache/p \
  -Doptimize=ReleaseFast \
  -Dcpu=baseline

%install

zig build install --prefix %{buildroot}%{_prefix} \
  --system /tmp/offline-cache/p \
  -Doptimize=ReleaseFast \
  -Dcpu=baseline

%files

%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{bash_completions_dir}/ghostty.bash
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{fish_completions_dir}/ghostty.fish
%{_datadir}/ghostty/doc/*
%{_datadir}/ghostty/*
%{_datadir}/icons/hicolor/*/apps/com.mitchellh.ghostty.png
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

%changelog
%autochangelog
