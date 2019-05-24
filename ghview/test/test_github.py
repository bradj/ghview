from ghview import github


def test_next_page(link_header_first, link_header_middle, link_header_last):
    control = 'https://api.github.com/organizations/913567/repos?per_page=100&page=2'
    result = github.next_page(link_header_first)

    assert(control == result)

    control = 'https://api.github.com/organizations/913567/repos?per_page=10&page=6'
    result = github.next_page(link_header_middle)

    assert(control == result)

    result = github.next_page(link_header_last)

    assert(result is None)


def test_check_throttle(new_obj):
    response = new_obj({'status_code': 403, 'headers': { 'X-RateLimit-Reset': 1558722877418/1000 }})

    github.check_throttle(response)
