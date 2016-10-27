#!/bin/sh
for WORKER in `transmission-remote  -l | grep 0.0 | cut -d' ' -f 3`;
do
    cat best-tracker.list | while read TRACKER;
    do
        echo "Adding $TRACKER";
        transmission-remote  -t ${WORKER} -td ${TRACKER};
    done
done

