Name:		mtn	
Version:	3.4.2
Release:	9%{?dist}
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

%if 0%{?mageia}
Requires:	ffmpeg
Requires:	fonts-ttf-dejavu
%else
Requires:	ffmpeg-libs
Requires:	dejavu-sans-fonts
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
%make_build
#fedora38, rhel9: /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf
#centos7: /usr/share/fonts/dejavu/DejaVuSans.ttf
#mageia:8 OK default
#rhel:8 OK default
#%make_build USER_CFLAGS=-DGB_F_FONTNAME=\\\"/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf\\\"

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
