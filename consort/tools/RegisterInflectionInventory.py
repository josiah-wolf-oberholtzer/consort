import abjad


class RegisterInflectionInventory(abjad.TypedList):

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PRIVATE PROPERTIES ###

    @property
    def _item_callable(self):
        import consort
        return consort.RegisterInflection
