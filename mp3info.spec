Summary:     Utility for MP3 information and tag modification
Summary(tr): MP3 ses dosyasý bilgileri düzenleme aracý
Summary(pl): Program do manipulowania tagami ID3 plików w formacie MP3.
Name:        mp3info
Version:     0.2.16
Release:     2
Copyright:   GPL
Source:      ftp://bimbo.hive.no/pub/mp3info/mp3info-%version.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Group:       Applications/Multimedia
Group(tr):   Uygulamalar/Çokluortam

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.

%description -l tr
mp3info, MP3 ses dosyalarýndan TAG (ID3) bilgilerini okumanýzý ve
deðiþtirmenizi saðlayan bir komut satýrý aracýdýr. Çeþitli þekillerde
çýktýlar verebilir.

%description -l pl
mp3info jest programem do manipulowania tagami ID3 plików w formacie MP3.
Umo¿liwia dowolne skonfigurowanie wy¶wietlanych przez to narzêdzie informacji.

%prep
%setup -q

%build
CXXFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s ./configure --prefix=/usr \
	--mandir=%{_mandir}
make

%install
%{__make} install prefix=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/%{_mandir}
gzip -9nf AUTHORS COPYING NEWS README ChangeLog mp3info.lsm
gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,NEWS,README,ChangeLog,mp3info.lsm}.gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/*/*
