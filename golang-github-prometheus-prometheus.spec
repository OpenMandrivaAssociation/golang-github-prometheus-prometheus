# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 1
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider        github
%global provider_tld    com
%global project         prometheus
%global repo            prometheus
# https://github.com/prometheus/prometheus
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          3569eef8b1bc062bb5df43181b938277818f365b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.8.0
Release:        3%{?dist}
Summary:        The Prometheus monitoring system and time series database
# Detected licences
# - *No copyright* Apache (v2.0) GENERATED FILE at 'LICENSE'
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if ! 0%{?with_bundled}
# cmd/prometheus/main.go
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/common/log)
BuildRequires: golang(github.com/prometheus/common/version)
BuildRequires: golang(golang.org/x/net/context)

# cmd/promtool/main.go
BuildRequires: golang(github.com/prometheus/common/version)

# cmd/prometheus/config.go
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/common/log)
BuildRequires: golang(github.com/prometheus/common/model)

# documentation/examples/remote_storage/remote_storage_adapter/main.go
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/golang/snappy)
BuildRequires: golang(github.com/influxdata/influxdb/client/v2)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/common/log)
BuildRequires: golang(github.com/prometheus/common/model)

# storage/local/storagetool/main.go
BuildRequires: golang(github.com/prometheus/common/version)

# documentation/examples/remote_storage/example_write_adapter/server.go
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/snappy)
BuildRequires: golang(github.com/prometheus/common/model)

# Remaining dependencies not included in main packages
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(github.com/opentracing/opentracing-go)
BuildRequires: golang(github.com/prometheus/client_model/go)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(k8s.io/client-go/kubernetes)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/compute)
BuildRequires: golang(k8s.io/client-go/tools/cache)
BuildRequires: golang(github.com/opentracing-contrib/go-stdlib/nethttp)
BuildRequires: golang(k8s.io/client-go/pkg/apis/extensions/v1beta1)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires: golang(k8s.io/client-go/pkg/api)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/servers)
BuildRequires: golang(github.com/prometheus/common/route)
BuildRequires: golang(github.com/gophercloud/gophercloud/pagination)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/samuel/go-zookeeper/zk)
BuildRequires: golang(github.com/prometheus/common/expfmt)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/filter)
BuildRequires: golang(k8s.io/client-go/rest)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/hashicorp/consul/api)
BuildRequires: golang(github.com/gophercloud/gophercloud)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/floatingips)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/network)
BuildRequires: golang(golang.org/x/net/netutil)
BuildRequires: golang(k8s.io/client-go/pkg/api/v1)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/hypervisors)
BuildRequires: golang(github.com/miekg/dns)
BuildRequires: golang(gopkg.in/fsnotify.v1)
%endif

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/compute)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/arm/network)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/snappy)
BuildRequires: golang(github.com/gophercloud/gophercloud)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/floatingips)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/hypervisors)
BuildRequires: golang(github.com/gophercloud/gophercloud/openstack/compute/v2/servers)
BuildRequires: golang(github.com/gophercloud/gophercloud/pagination)
BuildRequires: golang(github.com/hashicorp/consul/api)
BuildRequires: golang(github.com/influxdata/influxdb/client/v2)
BuildRequires: golang(github.com/miekg/dns)
BuildRequires: golang(github.com/opentracing-contrib/go-stdlib/nethttp)
BuildRequires: golang(github.com/opentracing/opentracing-go)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/client_model/go)
BuildRequires: golang(github.com/prometheus/common/expfmt)
BuildRequires: golang(github.com/prometheus/common/log)
BuildRequires: golang(github.com/prometheus/common/model)
BuildRequires: golang(github.com/prometheus/common/route)
BuildRequires: golang(github.com/prometheus/common/version)
BuildRequires: golang(github.com/samuel/go-zookeeper/zk)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/filter)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/net/netutil)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(gopkg.in/fsnotify.v1)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires: golang(k8s.io/client-go/kubernetes)
BuildRequires: golang(k8s.io/client-go/pkg/api)
BuildRequires: golang(k8s.io/client-go/pkg/api/v1)
BuildRequires: golang(k8s.io/client-go/pkg/apis/extensions/v1beta1)
BuildRequires: golang(k8s.io/client-go/rest)
BuildRequires: golang(k8s.io/client-go/tools/cache)
%endif

Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/compute)
Requires:      golang(github.com/Azure/azure-sdk-for-go/arm/network)
Requires:      golang(github.com/Azure/go-autorest/autorest/azure)
Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)
Requires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/aws/aws-sdk-go/service/ec2)
Requires:      golang(github.com/gogo/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/snappy)
Requires:      golang(github.com/gophercloud/gophercloud)
Requires:      golang(github.com/gophercloud/gophercloud/openstack)
Requires:      golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/floatingips)
Requires:      golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/hypervisors)
Requires:      golang(github.com/gophercloud/gophercloud/openstack/compute/v2/servers)
Requires:      golang(github.com/gophercloud/gophercloud/pagination)
Requires:      golang(github.com/hashicorp/consul/api)
Requires:      golang(github.com/influxdata/influxdb/client/v2)
Requires:      golang(github.com/miekg/dns)
Requires:      golang(github.com/opentracing-contrib/go-stdlib/nethttp)
Requires:      golang(github.com/opentracing/opentracing-go)
Requires:      golang(github.com/prometheus/client_golang/prometheus)
Requires:      golang(github.com/prometheus/client_model/go)
Requires:      golang(github.com/prometheus/common/expfmt)
Requires:      golang(github.com/prometheus/common/log)
Requires:      golang(github.com/prometheus/common/model)
Requires:      golang(github.com/prometheus/common/route)
Requires:      golang(github.com/prometheus/common/version)
Requires:      golang(github.com/samuel/go-zookeeper/zk)
Requires:      golang(github.com/syndtr/goleveldb/leveldb)
Requires:      golang(github.com/syndtr/goleveldb/leveldb/filter)
Requires:      golang(github.com/syndtr/goleveldb/leveldb/iterator)
Requires:      golang(github.com/syndtr/goleveldb/leveldb/opt)
Requires:      golang(github.com/syndtr/goleveldb/leveldb/util)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/net/context/ctxhttp)
Requires:      golang(golang.org/x/net/netutil)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/time/rate)
Requires:      golang(google.golang.org/api/compute/v1)
Requires:      golang(gopkg.in/fsnotify.v1)
Requires:      golang(gopkg.in/yaml.v2)
Requires:      golang(k8s.io/apimachinery/pkg/util/runtime)
Requires:      golang(k8s.io/client-go/kubernetes)
Requires:      golang(k8s.io/client-go/pkg/api)
Requires:      golang(k8s.io/client-go/pkg/api/v1)
Requires:      golang(k8s.io/client-go/pkg/apis/extensions/v1beta1)
Requires:      golang(k8s.io/client-go/rest)
Requires:      golang(k8s.io/client-go/tools/cache)

Provides:      golang(%{import_path}/config) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/azure) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/consul) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/dns) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/ec2) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/file) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/gce) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/kubernetes) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/marathon) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/openstack) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/triton) = %{version}-%{release}
Provides:      golang(%{import_path}/discovery/zookeeper) = %{version}-%{release}
Provides:      golang(%{import_path}/notifier) = %{version}-%{release}
Provides:      golang(%{import_path}/promql) = %{version}-%{release}
Provides:      golang(%{import_path}/relabel) = %{version}-%{release}
Provides:      golang(%{import_path}/retrieval) = %{version}-%{release}
Provides:      golang(%{import_path}/rules) = %{version}-%{release}
Provides:      golang(%{import_path}/storage) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/fanin) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/local) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/local/chunk) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/local/codable) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/local/index) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/metric) = %{version}-%{release}
Provides:      golang(%{import_path}/storage/remote) = %{version}-%{release}
Provides:      golang(%{import_path}/template) = %{version}-%{release}
Provides:      golang(%{import_path}/util/cli) = %{version}-%{release}
Provides:      golang(%{import_path}/util/flock) = %{version}-%{release}
Provides:      golang(%{import_path}/util/httputil) = %{version}-%{release}
Provides:      golang(%{import_path}/util/promlint) = %{version}-%{release}
Provides:      golang(%{import_path}/util/stats) = %{version}-%{release}
Provides:      golang(%{import_path}/util/strutil) = %{version}-%{release}
Provides:      golang(%{import_path}/util/testutil) = %{version}-%{release}
Provides:      golang(%{import_path}/util/treecache) = %{version}-%{release}
Provides:      golang(%{import_path}/web) = %{version}-%{release}
Provides:      golang(%{import_path}/web/api/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/web/ui) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/stretchr/testify/require)
BuildRequires: golang(github.com/stretchr/testify/suite)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1)
%endif

Requires:      golang(github.com/stretchr/testify/assert)
Requires:      golang(github.com/stretchr/testify/require)
Requires:      golang(github.com/stretchr/testify/suite)
Requires:      golang(k8s.io/apimachinery/pkg/apis/meta/v1)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
# No dependency directories so far
export GOPATH=$(pwd):%{gopath}
%endif

%gobuild -o bin/cmd/prometheus %{import_path}/cmd/prometheus
%gobuild -o bin/cmd/promtool %{import_path}/cmd/promtool
%gobuild -o bin/storage/local/storagetool %{import_path}/storage/local/storagetool

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/cmd/prometheus %{buildroot}%{_bindir}
install -p -m 0755 bin/cmd/promtool %{buildroot}%{_bindir}
install -p -m 0755 bin/storage/local/storagetool %{buildroot}%{_bindir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
for dir in retrieval/testdata discovery/file/fixtures storage/local/fixtures util/httputil; do
	mkdir -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $dir)
	cp -rpav $dir %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $dir)/.
	echo "%%{gopath}/src/%%{import_path}/$dir" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/cmd/prometheus
#%gotest %{import_path}/config
%gotest %{import_path}/discovery
%gotest %{import_path}/discovery/consul
#%gotest %{import_path}/discovery/file
%gotest %{import_path}/discovery/kubernetes
#%gotest %{import_path}/discovery/marathon
%gotest %{import_path}/discovery/openstack
%gotest %{import_path}/discovery/triton
%gotest %{import_path}/documentation/examples/remote_storage/remote_storage_adapter/graphite
%gotest %{import_path}/documentation/examples/remote_storage/remote_storage_adapter/influxdb
%gotest %{import_path}/documentation/examples/remote_storage/remote_storage_adapter/opentsdb
%gotest %{import_path}/notifier
%gotest %{import_path}/promql
%gotest %{import_path}/relabel
%gotest %{import_path}/retrieval
%gotest %{import_path}/rules
%gotest %{import_path}/storage/fanin
#%gotest %{import_path}/storage/local
%gotest %{import_path}/storage/local/chunk
%gotest %{import_path}/storage/local/codable
%gotest %{import_path}/storage/metric
%gotest %{import_path}/storage/remote
%gotest %{import_path}/template
%gotest %{import_path}/util/flock
%gotest %{import_path}/util/httputil
%gotest %{import_path}/util/promlint
%gotest %{import_path}/util/strutil
#%gotest %{import_path}/web
%gotest %{import_path}/web/api/v1
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md code-of-conduct.md CHANGELOG.md MAINTAINERS.md
%{_bindir}/prometheus
%{_bindir}/promtool
%{_bindir}/storagetool

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md code-of-conduct.md CHANGELOG.md MAINTAINERS.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md code-of-conduct.md CHANGELOG.md MAINTAINERS.md
%endif

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.8.0-1
- Update to 1.8.0
  resolves: #1495180

* Tue Aug 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.15.0-8
- Polish the spec file

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-1
- Update to 0.15.0
  resolves: #1246058

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 jchaloup <jchaloup@redhat.com> - 0.13.3-2
- Add debug info
  related: #1190426

* Tue May 12 2015 jchaloup <jchaloup@redhat.com> - 0.13.3-1
- Update to 0.13.3
  related: #1190426

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-1
- Update to 0.13.2
  related: #1190426

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4e6a807
- First package for Fedora
  resolves: #1190426
