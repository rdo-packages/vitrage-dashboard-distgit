%global pypi_name vitrage-dashboard
%global mod_name  vitrage_dashboard

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-vitrage-ui
Version:        XXX
Release:        XXX
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
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires: python-babel
Requires: openstack-dashboard
Requires: python-iso8601
Requires: python-keystoneclient
Requires: python-vitrageclient

%description
Vitrage Management Dashboard


%package doc
Summary: Documentation for Vitrage dashboard
%description doc
Documentation files for OpenStack Vitrage dashboard for Horizon


%prep
%setup -q -n vitrage-dashboard-%{upstream_version}
# Remove bundled egg-info
rm {test-,}requirements.txt

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

mv enabled/_4*.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/

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
