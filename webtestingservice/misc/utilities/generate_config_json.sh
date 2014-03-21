#!/bin/bash
dst_dir=/tmp/wts/harness
config_json_file=${dst_dir}/config.json
echo "[" > ${config_json_file}
cd ${dst_dir}/../suites/opt

for suite in `ls | grep -v testkit`
do
    echo '{"suite": "'${suite}'"},'
done | sed '$s/,//' >> ${config_json_file}

echo "]" >> ${config_json_file}
