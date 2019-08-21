# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sixfeetup.pmdashboard


class SixfeetupPmdashboardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sixfeetup.pmdashboard)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sixfeetup.pmdashboard:default')


SIXFEETUP_PMDASHBOARD_FIXTURE = SixfeetupPmdashboardLayer()


SIXFEETUP_PMDASHBOARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SIXFEETUP_PMDASHBOARD_FIXTURE,),
    name='SixfeetupPmdashboardLayer:IntegrationTesting',
)


SIXFEETUP_PMDASHBOARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SIXFEETUP_PMDASHBOARD_FIXTURE,),
    name='SixfeetupPmdashboardLayer:FunctionalTesting',
)


SIXFEETUP_PMDASHBOARD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SIXFEETUP_PMDASHBOARD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SixfeetupPmdashboardLayer:AcceptanceTesting',
)
