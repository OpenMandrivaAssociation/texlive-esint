# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/esint
# catalog-date 2006-10-27 00:09:51 +0200
# catalog-license pd
# catalog-version 1.1
Name:		texlive-esint
Version:	1.1
Release:	7
Summary:	Extended set of integrals for Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.source.tar.xz
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
%{_texmfdistdir}/fonts/source/public/esint/bigint.mf
%{_texmfdistdir}/fonts/source/public/esint/esint10.mf
%{_texmfdistdir}/fonts/source/public/esint/mathint.mf
%{_texmfdistdir}/fonts/tfm/public/esint/esint10.tfm
%{_texmfdistdir}/tex/latex/esint/esint.sty
%{_texmfdistdir}/tex/latex/esint/uesint.fd
%doc %{_texmfdistdir}/doc/latex/esint/README
%doc %{_texmfdistdir}/doc/latex/esint/esint.pdf
#- source
%doc %{_texmfdistdir}/source/latex/esint/esint.dtx
%doc %{_texmfdistdir}/source/latex/esint/esint.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751575
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718364
- texlive-esint
- texlive-esint
- texlive-esint
- texlive-esint

