# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global pypi_name vitrage-dashboard
%global mod_name  vitrage_dashboard

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-vitrage-ui
Version:        1.9.1
Release:        1%{?dist}
Summary:        Vitrage Management Dashboard

# bundled libraries:
# d3 is BSD licensed
# loadsh is MIT licensed
# graphlib is MIT licensed
# dagre is MIT licensed
License:        ASL 2.0 and BSD and MIT

URL:            https://github.com/openstack/vitrage-dashboard
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  git
BuildRequires:  openstack-macros

Requires: openstack-dashboard >= 1:14.0.0

Requires: python%{pyver}-iso8601
Requires: python%{pyver}-vitrageclient >= 2.5.0
Requires: python%{pyver}-django-compressor >= 2.0
Requires: python%{pyver}-django >= 1.8
Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-XStatic-Angular-Bootstrap >= 2.2.0.0
Requires: python%{pyver}-XStatic-Angular >= 1.5.8.0
Requires: python%{pyver}-XStatic-Bootstrap-SCSS >= 3.3.7.1
Requires: python%{pyver}-XStatic-Font-Awesome >= 4.7.0.0
Requires: python%{pyver}-XStatic-smart-table >= 1.4.13.2

# Handle python2 exception
%if %{pyver} == 2
Requires: python-XStatic-Bootstrap-Datepicker >= 1.3.1.0
Requires: python-XStatic-jQuery >= 1.8.2.1
%else
Requires: python%{pyver}-XStatic-Bootstrap-Datepicker >= 1.3.1.0
Requires: python%{pyver}-XStatic-jQuery >= 1.8.2.1
%endif

%description
Vitrage Management Dashboard


%package doc
Summary: Documentation for Vitrage dashboard
%description doc

Documentation files for OpenStack Vitrage dashboard for Horizon


%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Remove bundled egg-info
%py_req_cleanup

%build
%{pyver_build}

# Build html documentation
%{pyver_bin} setup.py build_sphinx
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%{pyver_install}

# Move config to horizon
mkdir -p  %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled
mkdir -p  %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled

mv vitrage_dashboard/enabled/_4*.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/

ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4000_project_vitrage_panel_group.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4000_project_vitrage_panel_group.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4010_project_topology_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4010_project_topology_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4020_project_alarms_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4020_project_alarms_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4030_project_entities_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4030_project_entities_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4040_project_template_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4040_project_template_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4100_admin_vitrage_panel_group.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4100_admin_vitrage_panel_group.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4110_admin_topology_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4110_admin_topology_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4120_admin_alarms_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4120_admin_alarms_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4130_admin_entities_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4130_admin_entities_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_4140_admin_template_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4140_admin_template_vitrage_panel.py


%files
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{mod_name}
%{pyver_sitelib}/*.egg-info

%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4000_project_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4010_project_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4020_project_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4030_project_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4040_project_template_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4100_admin_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4110_admin_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4130_admin_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4140_admin_template_vitrage_panel.py*

%{_sysconfdir}/openstack-dashboard/enabled/_4000_project_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4010_project_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4020_project_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4030_project_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4040_project_template_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4100_admin_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4110_admin_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4130_admin_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4140_admin_template_vitrage_panel.py*

%files doc
%doc doc/build/html
%license LICENSE

%changelog
* Wed Apr 03 2019 RDO <dev@lists.rdoproject.org> 1.9.1-1
- Update to 1.9.1

* Fri Mar 22 2019 RDO <dev@lists.rdoproject.org> 1.9.0-1
- Update to 1.9.0

