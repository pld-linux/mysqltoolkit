%include	/usr/lib/rpm/macros.perl
%define		pdir	mysqltoolkit
Summary:	MySQL Toolkit
Summary(pl.UTF-8):	MySQL Toolkit - zestaw narzędzi do MySQL-a
Name:		mysqltoolkit
Version:	1012
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/mysqltoolkit/%{name}-%{version}.tar.gz
# Source0-md5:	b4a919c97b220f5d986509583b6bce5d
URL:		http://mysqltoolkit.sourceforge.net/
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql >= 1.0
Requires:	perl-DBI >= 1.13
Requires:	perl-Term-ReadKey >= 2.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Toolkit is a collection of essential command-line utilities for
MySQL. Each is completely stand-alone, without dependencies other than
core Perl and the DBI drivers needed to connect to MySQL.

%description -l pl.UTF-8
MySQL Toolkit to zbiór ważnych narzędzi uruchamianych z linii poleceń
dla MySQL-a. Każde z nich jest w pełni samodzielne, bez zależności
większych niż podstawowa instalacja Perla i terowniki DBI potrzebne do
połączenia z bazą MySQL.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mysql-archiver
%attr(755,root,root) %{_bindir}/mysql-checksum-filter
%attr(755,root,root) %{_bindir}/mysql-deadlock-logger
%attr(755,root,root) %{_bindir}/mysql-duplicate-key-checker
%attr(755,root,root) %{_bindir}/mysql-find
%attr(755,root,root) %{_bindir}/mysql-heartbeat
%attr(755,root,root) %{_bindir}/mysql-parallel-dump
%attr(755,root,root) %{_bindir}/mysql-profile-compact
%attr(755,root,root) %{_bindir}/mysql-query-profiler
%attr(755,root,root) %{_bindir}/mysql-show-grants
%attr(755,root,root) %{_bindir}/mysql-slave-delay
%attr(755,root,root) %{_bindir}/mysql-slave-restart
%attr(755,root,root) %{_bindir}/mysql-table-checksum
%attr(755,root,root) %{_bindir}/mysql-table-sync
%attr(755,root,root) %{_bindir}/mysql-visual-explain
%{_mandir}/man1/mysql-archiver.1p*
%{_mandir}/man1/mysql-checksum-filter.1p*
%{_mandir}/man1/mysql-deadlock-logger.1p*
%{_mandir}/man1/mysql-duplicate-key-checker.1p*
%{_mandir}/man1/mysql-find.1p*
%{_mandir}/man1/mysql-heartbeat.1p*
%{_mandir}/man1/mysql-parallel-dump.1p*
%{_mandir}/man1/mysql-profile-compact.1p*
%{_mandir}/man1/mysql-query-profiler.1p*
%{_mandir}/man1/mysql-show-grants.1p*
%{_mandir}/man1/mysql-slave-delay.1p*
%{_mandir}/man1/mysql-slave-restart.1p*
%{_mandir}/man1/mysql-table-checksum.1p*
%{_mandir}/man1/mysql-table-sync.1p*
%{_mandir}/man1/mysql-visual-explain.1p*
%{_mandir}/man3/mysqltoolkit.3pm*
%{perl_vendorlib}/mysqltoolkit.pm
