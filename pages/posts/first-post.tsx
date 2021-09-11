import Head from 'next/head';
import Link from 'next/link';
import React from 'react';
import Layout from '../../components/layout';

const firstPost = 'First Post';

export default function FirstPost(): JSX.Element {
  return (
    <Layout>
      <Head>
        <title>{firstPost}</title>
      </Head>

      <h1>{firstPost}</h1>
      <h2>
        <Link href="/">
          <a>Back to Home</a>
        </Link>
      </h2>
    </Layout>
  );
}
