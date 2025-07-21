GH_ISSUE=`gh issue view 1 --json title,body`
GH_ISSUE_TITLE=$(echo $GH_ISSUE | jq -r '.title')
GH_ISSUE_BODY=$(echo $GH_ISSUE | jq -r '.body')
echo "Issue Title: $GH_ISSUE_TITLE"
echo "Issue Body: $GH_ISSUE_BODY"
gemini -s -y -p "$GH_ISSUE_BODY"