%define _prefix /var/lib/solr

Name:		solr
Version:	%{ver}
Release:	2%{?dist}
Summary:	Solr
License:	GPL
URL:		http://lucene.apache.org/solr/
Source: 	http://apache.cu.be/lucene/solr/%{version}/apache-solr-%{version}.tgz
Source1:        tomcat-solr.xml
Source2:        solrconfig.xml
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	/usr/sbin/groupadd /usr/sbin/useradd
Requires: 	tomcat6
BuildArch:	x86_64

%description
%{summary}
%
%prep
%setup -q -n apache-solr-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
%__install -d "%{buildroot}%{_prefix}"
cp -pr example/solr/* "%{buildroot}%{_prefix}"
rm %{buildroot}%{_prefix}/README.txt
cp -pr dist "%{buildroot}%{_prefix}"
cp -pr contrib "%{buildroot}%{_prefix}"
cp -p client/ruby/solr-ruby/solr/conf/schema.xml "%{buildroot}%{_prefix}"/conf
mkdir -p %{buildroot}/etc/tomcat6/Catalina/localhost/
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/etc/tomcat6/Catalina/localhost/solr.xml"
sed -i "s/VERSION/%{ver}/g" "%{buildroot}/etc/tomcat6/Catalina/localhost/solr.xml"
%__install -D -m0644 "%{SOURCE2}" %{buildroot}%{_prefix}/conf
%__install -d "%{buildroot}%{_prefix}"/data

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,tomcat,tomcat,-)
%attr(0755,tomcat,tomcat) %dir %{_prefix}
%doc
%config(noreplace) %{_prefix}/conf/schema.xml
%config(noreplace) %{_prefix}/conf/solrconfig.xml
%{_prefix}/solr.xml
/etc/tomcat6/Catalina/localhost/solr.xml
%{_prefix}/bin
%{_prefix}/conf
%{_prefix}/contrib
%{_prefix}/data
%{_prefix}/dist


%changelog
* Tue Jan 18 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation
