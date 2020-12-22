.. _story:

Stories
=======

The Lonely Script
------------------

This section tells the story of a lonely script in its object oriented world
of `Testbed`, `Conf` and `Ops` objects.

Once upon a time, there was a script. This script was lonely and invited a
`Testbed` to join in.

.. figure:: testbed.png
    :align: center
    :alt: A lonely testbed

This `Testbed` was charming, popular, and naturally, devices wanted to befriend
him. Eventually, two `Device` (PE1 and P1) decided to join the testbed.

.. figure:: testbed_devices.png
    :align: center
    :alt: Help them talk!

Each `Device` had a few of its own `Interface`s.

These two `Device` wanted to communicate with one another, but, sadly, they
could not reach each other. They needed some sort of `Link` to
communicate, though neither of them were capable of creating this `link`, as it
was outside of their responsibilities.

`Testbed` became determined to help the `Device` objects communicate.
`Testbed` worked quickly to create a `Link` to unite each `Device`.
With the `link` and an `Interface` from each `Device`, the `Devices` could
finally communicate with each other.

.. figure:: testbed_devices_link.png
    :align: center
    :alt: They can talk

Content that each `Device` could now communicate with the other,
`Testbed` thought it would be even better to create traffic. "Does anyone have
any ideas about how we could create some more traffic?", it said. "You need
me!", a bold, smart-sounding voice bellowed from the crowd. "I am a `Feature`,
put me each `Device` and I will create traffic."

.. figure:: device_feature.png
    :align: center
    :alt: New feature


As time passed, a new `Feature` approached `Testbed`, with a new, novel idea!
"Testbed?", it said. "I want to be applied to a Link." `Testbed` agreed, "What
an excellent idea!" So `Feature` applied itself to a `Link` knowing that the
moment it would, all `Interface` and `Device` within that `Link` that would be
able to clearly communicate.

.. figure:: device_feature_link.png
    :align: center
    :alt: New feature

Even though the 'Device's could communicate with one another, the script was
still lonely, as he could not undersand what they were saying. Almost as if
reading the script's thoughts, another voice, from the crowd, excitedly said,
"I can translate! I don't want to brag, but, I'm actually a genius." "Really?"
The script asked, hesitant to believe that someone could, finally, help it.
"You can help me?" "Of course I can", the voice from the crowd answered. "I'm
an `Ops` object, after all. I have the power to learn absolutely everything
there is to know about a particular feature and convert it into a
understandable structure. Once I do this, you will be able to undestand what
each device is saying."

Quickly, the `ops` object got to work and within no time, the script could
understand each 'Device'. "Finally", the script thought, "I'm not lonely
anymore."

.. note::

   As a part of the :ref:`abstraction <abstract>` package, all of Genie's objects,
    `Testbed`, `Device`, `Interface`, `Link` ,`Feature` and `ops`, work
    internally, enabling the agnostic infrastructure based.

Arthur: The Sandwich Lover
---------------------------

Arthur, a simple man, leading a simple life, had a unique love for all types of
sandwiches. To satisfy this love, Arthur began farming his own vegetables so
that he could enjoy the freshest, most delicious, vegetables on his sandwiches.

Each day, Arthur would work in his farm and he would harvest his vegetables so
that he could make his sandwich.

As time passed, Arthur discovered that the neighboring farms were growing
vegetables too. Some of their vegetables were different from the vegetables
Arthur grew. "Wouldn't it be nice to add eggplant to my sandwich?" Arthur,
thought. "But I can't possibly farm anymore vegetables, it would be far too
much work."

Arthur had an idea! He approached his farmer friend John; together, they
devised a plan where John would open a restaurant that would only make
sandwiches from the local farmers. All of the local farmers, including John,
would bring their harvested vegetables to John's restaurant at the end of each
day. John would then make all different sorts of delicious sandwiches using the
fresh vegetables from this pool of produce, and in return for their hard work,
serve the farmers.

Eventually, the farmers realized this model reduced their workload, increased
production and variation of vegetables, and reduced duplication of vegetables
between neighbors. Most importantly, the farmers were able to have more
varieties of vegetables in their daily sandwich!

.. note::

    The moral of this story, is that the restaurant represents the ``Genie``
    harness, the framework that brings various triggers and verifications to
    create a testscript.  When everyone contributes to this pool of
    triggers/verifications, larger selections of triggers/verifications will be
    available for the testing community.


