Name:		texlive-esint
Version:	52240
Release:	1
Summary:	Extended set of integrals for Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The esint package permits access to alternate integral symbols
when you're using the Computer Modern fonts. In the original
set, several integral symbols are missing, such as \oiint. Many
of these symbols are available in other font sets (pxfonts,
txfonts, etc.), but there is no good solution if you want to
use Computer Modern. The package provides Metafont source and
LaTeX macro support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/esint
%{_texmfdistdir}/fonts/tfm/public/esint
%{_texmfdistdir}/tex/latex/esint
%doc %{_texmfdistdir}/doc/latex/esint
#- source
%doc %{_texmfdistdir}/source/latex/esint

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
