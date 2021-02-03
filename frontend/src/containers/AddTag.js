import React, { useState } from 'react'
import {
  Container,
  Grid,
  makeStyles,
  TextField,
  Button,
  Typography,
  Paper,
  Select,
} from '@material-ui/core';
import { toast } from 'react-toastify';
import { connect } from 'react-redux';
import { createTag } from '../redux/actions/properties';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    direction: 'ltr',
  },
  background: {
    minHeight: `calc(100vh - 5em)`,
  },
  title: {
    fontSize: 40,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    margin: 'auto',
  },
}))

const Tag = ({ createTag }) => {
  const classes = useStyles();
  const [name, setName] = useState('')

  const handleSubmit = () => {
    if (!name) {
      toast.error('لطفاً عنوان تگ را وارد کن!');
      return;
    }
    createTag(name);
  }

  return (
    <div className={classes.root}>
      <Grid container justify='center' alignItems='center' className={classes.background}>
        <Grid
          xs={10}
          sm={6}
          item container
          justify='center'
          alignItems='stretch'
          direction='column'
          spacing={6}>
          <Grid item>
            <Typography gutterBottom variant='h3' className={classes.title} align='center'>
              افزودن تگ
            </Typography>
          </Grid>
          <Grid item >
            <Paper className={classes.paper}>
              <Grid
                container
                direction='column'
                justify='center'
                spacing={2}>
                <Grid item>
                  <TextField
                    label='عنوان'
                    variant='outlined'
                    gutterBottom
                    fullWidth
                    onChange={(e) => setName(e.target.value)}
                  />
                </Grid>
                <Grid container item alignItems='center' justify='center' spacing={2}>
                  <Grid item>
                    <Button onClick={handleSubmit} variant='contained' color='primary'>
                      ثبت
                    </Button>
                  </Grid>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </Grid>
    </div>
  )
}

const mapStateToProps = (state, ownProps) => ({

})

export default connect(
  mapStateToProps,
  {
    createTag,
  }
)(Tag);