Summary:	Utility for MP3 information and tag modification
Summary(pl):	Program do manipulowania tagami ID3 plików w formacie MP3
Summary(tr):	MP3 ses dosyasý bilgileri düzenleme aracý
Name:		mp3info
Version:	0.2.16
Release:	6
License:	GPL
Group:		Applications/Sound
Source0:	ftp://bimbo.hive.no/pub/mp3info/%{name}-%{version}.tar.bz2
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

%description -l pl
mp3info jest programem do manipulowania tagami ID3 plików w formacie
MP3. Umo¿liwia dowolne skonfigurowanie wy¶wietlanych przez to
narzêdzie informacji.

%description -l tr
mp3info, MP3 ses dosyalarýndan TAG (ID3) bilgilerini okumanýzý ve
deðiþtirmenizi saðlayan bir komut satýrý aracýdýr. Çeþitli þekillerde
çýktýlar verebilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CXX="%{__cc}"; export CXX
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
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
