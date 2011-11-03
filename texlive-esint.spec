# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/esint
# catalog-date 2006-10-27 00:09:51 +0200
# catalog-license pd
# catalog-version 1.1
Name:		texlive-esint
Version:	1.1
Release:	1
Summary:	Extended set of integrals for Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The esint package permits access to alternate integral symbols
when you're using the Computer Modern fonts. In the original
set, several integral symbols are missing, such as \oiint. Many
of these symbols are available in other font sets (pxfonts,
txfonts, etc.), but there is no good solution if you want to
use Computer Modern. The package provides Metafont source and
LaTeX macro support.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
