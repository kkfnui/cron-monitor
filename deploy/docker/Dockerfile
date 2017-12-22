FROM centos:centos7


# tools
RUN yum -y update; yum clean all
RUN yum -y install python-pip python-django git sqlite; yum clean all

# code folder
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN git clone -b release git@192.168.0.3:server/cron-monitor.git
WORKDIR /usr/src/cron-monitor



WORKDIR /usr/src/cron-monitor/server/web
# start mail
EXPOSE 8080
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8080", "--settings=settings.dev"]