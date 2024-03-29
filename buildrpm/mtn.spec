Name:		mtn	
Version:	3.5.0
Release:	1%{?dist}
Summary:	Movie thumbnailer

License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/devel/%{name}-devel.tar.gz
# Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/v%%{version}/%%{name}-v%%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gd-devel >= 2.0.35
BuildRequires:	ffmpeg-devel >= 3.3.1

Requires:	gd
Requires:   fontconfig

%if 0%{?mageia}
Requires:	ffmpeg
Requires:	fonts-ttf-dejavu
%else
Requires:	ffmpeg-libs
Requires:	dejavu-sans-fonts
%endif

%if %{?mageia}%{!?mageia:100} <= 8 || %{?rhel}%{!?rhel:100} <= 8
%define with_avif ENABLE_AVIF=0
%endif

%if %{?rhel}%{!?rhel:100} <= 7
%define with_webp ENABLE_WEBP=0
%endif

%description
Movie thumbnail generator

%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: bash-completion
Requires: fontconfig
# Does not work on centOS7
# Enhances: mtn

%description bash-completion
Bash completion support for the %{name}'s utilities.

%package zsh-completion
Summary: Zsh completion support for %{name}
BuildArch: noarch
Requires: zsh
Requires: fontconfig
# Does not work on centOS7
# Enhances: mtn

%description zsh-completion
Zsh completion support for the %{name}'s utilities.

%prep
tar -xf %SOURCE0
cd %{name}-*
#%%setup -n %%{name}-devel

%build
cd %{name}-*/src
%make_build %?with_webp %?with_avif

%install
cd %{name}-*/src
%make_install PREFIX=%{_prefix}

## Make bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 ../completions/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -pm644 ../completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%{_bindir}/mtn
%{_defaultdocdir}/mtn
%{_mandir}/man1/mtn.1*
%license %{name}*/LICENSE

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%clean
rm -rf %{buildroot}

%changelog
* Mon Feb 26 2024 wahibre <wahibre@gmx.com> - 3.5.0-1
- update to new version

* Tue May 16 2023 wahibre <wahibre@gmx.com> - 3.4.2-2
- building with avif and webp

* Mon Feb 14 2022 wahibre <wahibre@gmx.com> - 3.4.2-1
- update to version 3.4.2

* Tue Mar 02 2021 wahibre <wahibre@gmx.com> - 3.4.1-2
- fix font dependency for Mageia

* Thu Feb 25 2021 wahibre <wahibre@gmx.com> - 3.4.1-1
- update to version 3.4.1

* Tue May 05 2020 wahibre <wahibre@gmx.com> - 3.3.3-3
- removed Enhances
- Add dejavu-sans-fonts to Requires
- bash completion
- zsh completion

* Thu May 30 2019 wahibre <wahibre@gmx.com> - 3.3.2
- add install prefix

* Mon Aug 7 2017 wahibre <wahibre@gmx.com> - 3.0
- initial
