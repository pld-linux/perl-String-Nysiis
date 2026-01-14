#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	String
%define		pnam	Nysiis
Summary:	String::Nysiis - NYSIIS phonetic encoding
Summary(pl.UTF-8):	String::Nysiis - kodowanie fonetyczne NYSIIS
Name:		perl-String-Nysiis
Version:	1.00
Release:	5
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	388864350483b557f478c300f040e8de
URL:		http://search.cpan.org/dist/String-Nysiis/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
New York State Identification and Intelligence System (NYSIIS)
algorithm for phonetic encoding of names.

%description -l pl.UTF-8
Algorytm NYSIIS (New York State Identification and Intelligence
System) do fonetycznego kodowania nazw.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
