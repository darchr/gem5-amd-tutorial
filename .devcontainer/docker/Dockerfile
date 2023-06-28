FROM gcr.io/gem5-test/ubuntu-22.04_all-dependencies:latest as builder

RUN git clone -b release-staging-v23-0 https://github.com/gem5/gem5.git
WORKDIR /gem5
RUN scons build/ALL/gem5.opt

FROM gcr.io/gem5-test/ubuntu-22.04_all-dependencies:latest
COPY --from=builder /gem5/build/ALL/gem5.opt /bin/gem5
