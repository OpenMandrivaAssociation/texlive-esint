%global tl_name esint
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2d
Release:	%{tl_revision}.1
Summary:	Extended set of integrals for Computer Modern
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esint
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The esint package permits access to alternate integral symbols when you
are using the Computer Modern fonts. In the original set, several
integral symbols are missing, such as \oiint. Many of these symbols are
available in other font sets (pxfonts, txfonts, etc.), but there is no
good solution if you want to use Computer Modern. The package provides
Metafont source and LaTeX macro support.

