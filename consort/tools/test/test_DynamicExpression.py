# -*- encoding: utf-8 -*-
import consort
from abjad.tools import scoretools
from abjad.tools import systemtools


def test_DynamicExpression_01():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \<
                f'4
            }
            {
                g'4 \mf
                a'4
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \<
                f'4
            }
            {
                g'4 \mf
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \<
                f'4 \mf
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4 \p
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f
            }
        }
        ''')


def test_DynamicExpression_02():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf
                f'4
            }
            {
                g'4 \>
                a'4 \mp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf
                f'4
            }
            {
                g'4
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf
                f'4
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4 \mf
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p
            }
        }
        ''')


def test_DynamicExpression_03():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        start_dynamic_tokens="fff fffff",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4
            }
            {
                g'4 \p \<
                a'4 \mf
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4
            }
            {
                g'4 \p
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4 \p
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4 \f
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff
            }
        }
        ''')


def test_DynamicExpression_04():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        stop_dynamic_tokens="ppp ppppp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \<
                f'4
            }
            {
                g'4 \mf \>
                a'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \>
                f'4
            }
            {
                g'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \p \>
                f'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4
            }
            {
                e'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \f \>
                d'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \ppp
            }
        }
        ''')


def test_DynamicExpression_05():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        stop_dynamic_tokens="ppp ppppp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf
                f'4
            }
            {
                g'4 \>
                a'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf \>
                f'4
            }
            {
                g'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \<
                d'4
            }
            {
                e'4 \mf \>
                f'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \>
                d'4
            }
            {
                e'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \p \>
                d'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \ppppp
            }
        }
        ''')


def test_DynamicExpression_06():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        start_dynamic_tokens="fff fffff",
        stop_dynamic_tokens="ppp ppppp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4
            }
            {
                g'4 \p \>
                a'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4
            }
            {
                g'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \f \>
                f'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4
            }
            {
                e'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff \>
                d'4 \ppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fff
            }
        }
        ''')


def test_DynamicExpression_07():
    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens="f p mf mf mp",
        start_dynamic_tokens="fff fffff",
        stop_dynamic_tokens="ppp ppppp",
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff \>
                d'4
            }
            {
                e'4 \p \<
                f'4
            }
            {
                g'4 \mf \>
                a'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' } { g' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff \>
                d'4
            }
            {
                e'4 \p \>
                f'4
            }
            {
                g'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' f' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff \>
                d'4
            }
            {
                e'4 \p \>
                f'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' } { e' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff \>
                d'4
            }
            {
                e'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' d' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff \>
                d'4 \ppppp
            }
        }
        ''')

    music = scoretools.Staff("{ c' }")
    dynamic_expression(music, seed=1)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                c'4 \fffff
            }
        }
        ''')

def test_DynamicExpression_08():

    dynamic_expression = consort.DynamicExpression(
        dynamic_tokens='p ppp',
        start_dynamic_tokens='niente',
        stop_dynamic_tokens='niente',
        )

    music = scoretools.Staff("{ c' d' } { e' f' } { g' a' }")
    dynamic_expression(music)
    assert format(music) == systemtools.TestManager.clean_string(
        r'''
        \new Staff {
            {
                \once \override Hairpin.circled-tip = ##t
                c'4 \<
                d'4
            }
            {
                e'4 \p \>
                f'4
            }
            {
                \once \override Hairpin.circled-tip = ##t
                g'4 \ppp \>
                a'4 \!
            }
        }
        ''')
