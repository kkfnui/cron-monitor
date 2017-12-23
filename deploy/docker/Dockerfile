FROM centos:centos7


# tools
RUN yum -y update; yum clean all
RUN yum -y install epel-release
RUN yum -y install which python python-pip git sqlite; yum clean all
RUN mkdir -p ~/.pip/
RUN echo -e "[global]\nindex-url = http://mirrors.aliyun.com/pypi/simple/\n\n[install]\ntrusted-host=mirrors.aliyun.com" > ~/.pip/pip.conf
RUN pip install --upgrade pip
# code folder
RUN mkdir -p /usr/src
WORKDIR /usr/src

RUN git clone -b master https://github.com/kkfnui/cron-monitor.git
WORKDIR /usr/src/cron-monitor/server/web
RUN pip install -r requirements.txt
# start mail
EXPOSE 8080
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8080", "--settings=settings.dev"]