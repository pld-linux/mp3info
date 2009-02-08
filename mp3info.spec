Summary:	Utility for MP3 information and tag modification
Summary(hu.UTF-8):	Eszköz MP3 információk és tag módosítására
Summary(pl.UTF-8):	Program do manipulowania tagami ID3 plików w formacie MP3
Summary(tr.UTF-8):	MP3 ses dosyası bilgileri düzenleme aracı
Name:		mp3info
Version:	0.2.16
Release:	7
License:	GPL v2
Group:		Applications/Sound
# originally from ftp://bimbo.hive.no/pub/mp3info/ (dead)
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	ef1b3d9b83d2918699de60942fe8d5b5
Patch0:		%{name}-aclocal.patch
Patch1:		%{name}-time.h.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.

%description -l hu.UTF-8
mp3info egy parancssoros eszköz TAG (ID3) informácikók kinyerésére és
szerkesztésére MP3 fájlokban. A kimenete is konfigurálható.

%description -l pl.UTF-8
mp3info jest programem do manipulowania tagami ID3 plików w formacie
MP3. Umożliwia dowolne skonfigurowanie wyświetlanych przez to
narzędzie informacji.

%description -l tr.UTF-8
mp3info, MP3 ses dosyalarından TAG (ID3) bilgilerini okumanızı ve
değiştirmenizi sağlayan bir komut satırı aracıdır. Çeşitli şekillerde
çıktılar verebilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/mp3info
%{_mandir}/man1/mp3info.1*
