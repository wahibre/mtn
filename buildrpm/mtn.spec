Name:		mtn	
Version:	3.3.3
Release:	6%{?dist}
Summary:	Movie thumbnailer

License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/devel/%{name}-devel.tar.gz
# Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/%%{version}/%%{name}-%%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gd-devel >= 2.0.35
BuildRequires:	ffmpeg-devel >= 3.3.1

Requires:	gd
Requires:	dejavu-sans-fonts

%if 0%{?mageia}
Requires:	ffmpeg
%else
Requires:	ffmpeg-libs
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
cd %{name}-devel
#%%setup -n %%{name}-devel

%build
cd %{name}-devel/src
%make_build

%install
cd %{name}-devel/src
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

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%clean
rm -rf %{buildroot}

%changelog
* Tue May 05 2020 wahibre  <wahibre@gmx.com> - 3.3.3-3
- removed Enhances
- Add dejavu-sans-fonts to Requires
- bash completion
- zsh completion

* Thu May 30 2019 wahibre  <wahibre@gmx.com> - 3.3.2
- add install prefix

* Mon Aug 7 2017 wahibre  <wahibre@gmx.com> - 3.0
- initial
