import pytest
from git_identity_tools.path_utils import get_org_and_enterprise


@pytest.mark.parametrize("base_path, repo_path, expected", [
    # Case: personal repo (flat structure)
    ("/Users/rama/source", "/Users/rama/source/art-cmyk/my-project", ("art-cmyk", "art-cmyk")),

    # Case: enterprise repo (nested structure)
    ("/Users/rama/source", "/Users/rama/source/Microsoft/jesse-ai/ai-insights", ("jesse-ai", "Microsoft")),

    # Case: invalid/too shallow path
    ("/Users/rama/source", "/Users/rama/source", (None, None)),

    # Case: one-level deep folder only
    ("/Users/rama/source", "/Users/rama/source/just-one", ("just-one", "just-one")),

    # Case: deep nesting beyond org
    ("/Users/rama/source", "/Users/rama/source/Foo/Bar/Baz/Repo", ("Bar", "Foo")),  # based only on first 3
])
def test_get_org_and_enterprise(base_path, repo_path, expected):
    assert get_org_and_enterprise(repo_path, base_path) == expected
