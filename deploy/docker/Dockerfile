FROM centos:centos7


# tools
RUN yum -y update; yum clean all
RUN yum -y install epel-release
RUN yum -y install which python python-pip python-django git sqlite; yum clean all

# code folder
RUN which python
RUN which pip
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN git clone https://github.com/kkfnui/cron-monitor.git
WORKDIR /usr/src/cron-monitor
WORKDIR /usr/src/cron-monitor/server/web
RUN pip install -r requirements.txt
# start mail
EXPOSE 8080
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8080", "--settings=settings.dev"]