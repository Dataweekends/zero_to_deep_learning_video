FROM continuumio/miniconda3:4.3.14

ENTRYPOINT ["/bin/bash", "-c" ]

RUN groupadd -r course -g 1000 && useradd -u 1000 -r -g course -m -d /course -s /sbin/nologin -c "Course user" course && \
    chmod 755 /course

RUN git clone https://github.com/Dataweekends/zero_to_deep_learning_udemy /course/zero_to_deep_learning_udemy
WORKDIR /course/zero_to_deep_learning_udemy
RUN conda env create
RUN chown -R course:course .

USER course
CMD ["source activate ztdl && jupyter notebook --ip='*' --port=8888 --no-browser"]