#!/bin/bash

BASE_DIR="$(dirname $0)"
REPO_PATH="${BASE_DIR}/.."
ARCH="${1}"
IMAGE="${2}"
VERSION="${3}"

[[ $ARCH ]] || ARCH="x86"

tag_and_push() {
  docker tag "comworkio/${2}:latest" "comworkio/${2}:${1}"
  docker push "comworkio/${2}:${1}"
}

cd "${REPO_PATH}" && git pull origin main || : 
git config --global user.email "${GIT_EMAIL}"
git config --global user.name "${GIT_EMAIL}"
sha="$(git rev-parse --short HEAD)"
echo '{"version":"'"${VERSION}"'", "sha":"'"${sha}"'", "arch":"'"${ARCH}"'"}' > manifest.json

docker_compose_file="docker-compose.yml"
[[ -f docker-compose-build-${ARCH}.yml ]] && docker_compose_file="docker-compose-build-${ARCH}.yml"

COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose -f "${docker_compose_file}" build "${IMAGE}"

echo "${DOCKER_ACCESS_TOKEN}" | docker login --username "${DOCKER_USERNAME}" --password-stdin

[[ $ARCH == "x86" ]] && tag_and_push "latest" "${IMAGE}"
[[ $ARCH == "x86" ]] && tag_and_push "${VERSION}" "${IMAGE}"
tag_and_push "latest-${ARCH}" "${IMAGE}"
tag_and_push "${VERSION}-${ARCH}" "${IMAGE}"
tag_and_push "${VERSION}-${ARCH}-${CI_COMMIT_SHORT_SHA}" "${IMAGE}"

exit 0
