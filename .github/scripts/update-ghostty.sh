#!/usr/bin/env bash

latest=$(gh api repos/ghostty-org/ghostty/tags --jq .[0].name)
version=${latest#v}

spec=${GITHUB_WORKSPACE}/ghostty.spec

if grep -q "%global ver $version" "${spec}"; then
    echo "ghostty.spec is already at version $version."
    exit 0
fi

echo "Updating ghostty.spec to $version."
sed -i "s/%global ver .*/%global ver ${version}/g" "${spec}"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git add -u
git commit -m "Update to ghostty $latest"
git push