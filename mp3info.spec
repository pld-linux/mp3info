Summary:	Utility for MP3 information and tag modification
Summary(tr):	MP3 ses dosyasý bilgileri düzenleme aracý
Summary(pl):	Program do manipulowania tagami ID3 plików w formacie MP3.
Name:		mp3info
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Version:	0.2.16
Release:	3
License:	GPL
Source0:	ftp://bimbo.hive.no/pub/mp3info/%{name}-%{version}.tar.bz2
Patch0:		%{name}-aclocal.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.

%description -l tr
mp3info, MP3 ses dosyalarýndan TAG (ID3) bilgilerini okumanýzý ve
deðiþtirmenizi saðlayan bir komut satýrý aracýdýr. Çeþitli þekillerde
çýktýlar verebilir.

%description -l pl
mp3info jest programem do manipulowania tagami ID3 plików w formacie
MP3. Umo¿liwia dowolne skonfigurowanie wy¶wietlanych przez to
narzêdzie informacji.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS=-s; export LDFLAGS
aclocal
autoconf
automake
autoheader
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS COPYING NEWS README ChangeLog \
	$RPM_BUILD_ROOT/%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
