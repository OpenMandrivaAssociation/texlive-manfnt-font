%global tl_name manfnt-font
%global tl_revision 45777

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Knuths manual fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/manual
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manfnt-font.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Metafont (by Donald Knuth) and Adobe Type 1 (by Taco Hoekwater) versions
of the font containing the odd symbols Knuth uses in his books. LaTeX
support is available using the manfnt package


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from manfnt-font:
MixedMap manfnt.map
TL_DROPIN_EOF
