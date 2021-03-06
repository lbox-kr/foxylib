#!/bin/bash -f

set -e
set -u

FILE_PATH=$(readlink -f $0)
FILE_NAME=$(basename $FILE_PATH)
FILE_DIR=$(dirname $FILE_PATH)
# FILE_DIR=`pwd`/../scripts/test
SCRIPTS_DIR=$FILE_DIR

errcho(){ >&2 echo $@; }
func_count2reduce(){
    local v="${1?missing}"; local cmd="${2?missing}"; local n=${3?missing};
    for ((i=0;i<$n;i++)); do v=$($cmd $v) ; done; echo "$v"
}

REPO_DIR=$(func_count2reduce $FILE_DIR dirname 1)


unittest(){
    # python -m unittest foxylib.tools.jinja2.tests.test_jinja2_tool
    # python -m unittest foxylib.tools.jinja2.tests.test_jinja2_tool
    #python -m unittest foxylib.tools.collections.tests.test_collections_tool.LLToolkitTest.test_02
    python -m unittest foxylib.tools.html.test.test_html_tool.TestHTMLTool
    # python -m unittest foxylib.tools.hangeul.tests.test_hangeul_tool.HangeulToolTest.test_01
    # python -m unittest foxylib.tools.process.tests.test_process_tool.ProcessToolTest.test_01
    #python -m unittest foxylib.tools.span.tests.test_span_tool.TestSpanTool.test_01
    # python -m unittest foxylib.tools.collections.tests.test_chunk_tool TestChunkTool.test_02
}

main(){
    pushd $REPO_DIR

    unittest
    # pytest

    popd
}

main
