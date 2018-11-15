Name:        tower-dashboard
Version:     0.0.1
Release:     1.VERS%{?dist}
Summary:     Ansible Tower QE Dashboards
License:     ASL 2.0
URL:         https://github.com/Spredzy/tower-dashboard
Source0:     towerdashboard-%{version}.tar.gz

BuildArch:   noarch

BuildRequires:  python2-setuptools
BuildRequires:  python2-rpm-macros

Requires:    python-flask
Requires:    python-requests

%description
Dashboard to have an overview of the current state of the things
Ansible Tower QE related.


%prep
%autosetup -n towerdashboard-%{version}


%build
%py2_build


%install
%py2_install
install -d %{buildroot}/%{_datarootdir}/tower-dashboard
install -d %{buildroot}/%{_sysconfdir}/tower-dashboard
cp ./towerdashboard/schema.sql %{buildroot}/%{python2_sitelib}/towerdashboard/schema.sql
cp -r ./towerdashboard/templates %{buildroot}/%{python2_sitelib}/towerdashboard/
cp -r ./towerdashboard/static %{buildroot}/%{python2_sitelib}/towerdashboard/
cp ./wsgi.py %{buildroot}/%{_datarootdir}/tower-dashboard/wsgi.py
cp ./towerdashboard/settings/settings.py %{buildroot}/%{_sysconfdir}/tower-dashboard/
rm %{buildroot}/%{python2_sitelib}/towerdashboard/settings/settings.py
%{__ln_s} %{_sysconfdir}/tower-dashboard/settings.py %{buildroot}/%{python2_sitelib}/towerdashboard/settings/settings.py


%files
%doc README.md
%license LICENSE
%{python2_sitelib}/*
%{_datarootdir}/tower-dashboard/wsgi.py
%config(noreplace) %{_sysconfdir}/tower-dashboard/settings.py
%exclude %{_sysconfdir}/tower-dashboard/settings.py?
%exclude %{python2_sitelib}/towerdashboard/settings/settings.py?
%exclude %{_datarootdir}/tower-dashboard/wsgi.py?


%changelog
* Wed Nov 14 2018 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
