%global octpkg datatypes

Summary:	Extra data types for GNU Octave
Name:		octave-datatypes
Version:	1.0.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/datatypes/
Url:		https://github.com/pr0m1th3as/datatypes/
Source0:	https://github.com/pr0m1th3as/datatypes/archive/refs/tags/release-%{version}.tar.gz

BuildRequires:  octave-devel >= 9.1.0
# tests
BuildRequires:  timezone

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%patchlist
datatypes-1.0.2-fix_build.patch

%description
Extra data types for GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-release-%{version}

%build
export CXXFLAGS="%optflags -std=c++20"
export LDFLAGS="%ldflags `pkg-config --libs libcurl`"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
# some tests fail on ABF because they try to downloadtzdata fom internt
%octave_pkg_check || :

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

