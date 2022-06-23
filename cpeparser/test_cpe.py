from cpeparser import CpeParser


def test_parser():
    cpe = CpeParser()
    assert cpe.parser("cpe:2.3:a:ipython:ipython:*:*:*:*:*:*:*:*") == {
        'part': 'a',
        'vendor': 'ipython',
        'product': 'ipython',
        'version': '*',
        'update': '*',
        'edition': '*',
        'language': '*',
        'sw_edition': '*',
        'target_sw': '*',
        'target_hw': '*',
        'other': '*'}
    assert cpe.parser("cpe:2.3:a:istio:istio:1.12.1:*:*:*:*:*:*:*") == {
        'part': 'a',
        'vendor': 'istio',
        'product': 'istio',
        'version': '1.12.1',
        'update': '*',
        'edition': '*',
        'language': '*',
        'sw_edition': '*',
        'target_sw': '*',
        'target_hw': '*',
        'other': '*'}
    assert cpe.parser("cpe:/a:tester:new:1.3.2:*:*:*:*:webflow:*:*") == {
        'part': 'a',
        'vendor': 'tester',
        'product': 'new',
        'version': '1.3.2',
        'update': '*',
        'edition': '*',
        'language': '*',
        'sw_edition': '*',
        'target_sw': 'webflow',
        'target_hw': '*',
        'other': '*'}
