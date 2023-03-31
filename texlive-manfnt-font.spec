Name:		texlive-manfnt-font
Version:	45777
Release:	2
Summary:	Knuth's "manual" fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/manfnt-font
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manfnt-font.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Metafont (by Donald Knuth) and Adobe Type 1 (by Taco Hoekwater)
versions of the font containing the odd symbols Knuth uses in
his books. LaTeX support is available using the manfnt package

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/hoekwater/manfnt-font
%{_texmfdistdir}/fonts/map/dvips/manfnt-font
%{_texmfdistdir}/fonts/afm/hoekwater/manfnt-font

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
