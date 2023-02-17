ARG RUST_IMAGE_VERSION=latest

FROM rust:${RUST_IMAGE_VERSION} as builder
WORKDIR /tmp/build
COPY . .
RUN apt-get update && apt-get install -y cmake g++ libprotobuf-dev protobuf-compiler
# RUN cargo build --release

FROM ubuntu as datenlord
LABEL maintainers="DatenLord Authors"
LABEL description="DatenLord Distributed Storage"

COPY --from=builder ./target/release/datenlord /usr/local/bin/datenlord
COPY --from=builder ./scripts/umount-in-container.sh /usr/local/bin/umount-in-container.sh
COPY --from=builder ./scripts/datenlord-entrypoint.sh /usr/local/bin/datenlord-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/datenlord-entrypoint.sh"]
CMD []
