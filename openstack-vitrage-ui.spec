%global pypi_name vitrage-dashboard
%global mod_name  vitrage_dashboard

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-vitrage-ui
Version:        1.4.2
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

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  git
BuildRequires:  openstack-macros

Requires: openstack-dashboard >= 1:13.0.0

Requires: python2-iso8601
Requires: python2-vitrageclient
Requires: python2-django-compressor >= 2.0
Requires: python2-django >= 1.8
Requires: python2-pbr >= 2.0.0

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
%{__python2} setup.py build

# Build html documentation
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

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


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{mod_name}
%{python2_sitelib}/*.egg-info

%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4000_project_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4010_project_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4020_project_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4030_project_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4040_project_template_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4100_admin_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4110_admin_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_4130_admin_entities_vitrage_panel.py*

%{_sysconfdir}/openstack-dashboard/enabled/_4000_project_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4010_project_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4020_project_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4030_project_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4040_project_template_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4100_admin_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4110_admin_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4120_admin_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_4130_admin_entities_vitrage_panel.py*

%files doc
%doc doc/build/html
%license LICENSE

%changelog
* Wed Feb 21 2018 RDO <dev@lists.rdoproject.org> 1.4.2-1
- Update to 1.4.2

* Sat Feb 17 2018 RDO <dev@lists.rdoproject.org> 1.4.1-1
- Update to 1.4.1

