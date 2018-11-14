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


%files
%doc README.md
%license LICENSE
%{python2_sitelib}/*


%changelog
* Wed Nov 14 2018 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
