Summary:	Utility for MP3 information and tag modification
Summary(pl):	Program do manipulowania tagami ID3 plik�w w formacie MP3
Summary(tr):	MP3 ses dosyas� bilgileri d�zenleme arac�
Name:		mp3info
Version:	0.2.16
Release:	5
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/D�wi�k
Group(pt_BR):	Aplica��es/Som
Source0:	ftp://bimbo.hive.no/pub/mp3info/%{name}-%{version}.tar.bz2
Patch0:		%{name}-aclocal.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.

%description -l pl
mp3info jest programem do manipulowania tagami ID3 plik�w w formacie
MP3. Umo�liwia dowolne skonfigurowanie wy�wietlanych przez to
narz�dzie informacji.

%description -l tr
mp3info, MP3 ses dosyalar�ndan TAG (ID3) bilgilerini okuman�z� ve
de�i�tirmenizi sa�layan bir komut sat�r� arac�d�r. �e�itli �ekillerde
��kt�lar verebilir.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
